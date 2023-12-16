
module "network" {
  //source = "git@github.com:FairwindsOps/terraform-gcp-vpc-native.git//default?ref=default-v2.1.0"
  source = "./github/terraform-gcp-vpc-native/default"
  // base network parameters
  network_name     = "kube"
  subnetwork_name  = "kube-subnet"
  region           = "us-central1"
  //enable_flow_logs = "false"
  // subnetwork primary and secondary CIDRS for IP aliasing
  subnetwork_range    = "10.40.0.0/16"
  subnetwork_pods     = "10.41.0.0/16"
  subnetwork_services = "10.42.0.0/16"
}

module "cluster" {
  //source                           = "git@github.com:FairwindsOps/terraform-gke.git//vpc-native?ref=vpc-native-v1.2.0"
  source                           = "./github/terraform-gke/vpc-native"
  region                           = "us-central1"
  name                             = "gke-example"
  project                          = "terraform-module-cluster"
  network_name                     = "kube"
  //nodes_subnetwork_name            = module.network.subnetwork_name
  nodes_subnetwork_name            = "kube-subnet"
  //kubernetes_version               = "1.16.10-gke.8" BUGBUG
  // BUGBUG checkout: https://cloud.google.com/kubernetes-engine/docs/release-notes
  kubernetes_version               = "1.22.12-gke.300"
  pods_secondary_ip_range_name     = module.network.gke_pods_1
  services_secondary_ip_range_name = module.network.gke_services_1
}

module "node_pool" {
//  source             = "git@github.com:/FairwindsOps/terraform-gke//node_pool?ref=node-pool-v3.0.0"
  source             = "./github/terraform-gke-node_pool/node_pool"
  name               = "gke-example-node-pool"
  region             = module.cluster.region
  gke_cluster_name   = module.cluster.name
  machine_type       = "n1-standard-4"
  min_node_count     = "1"
  max_node_count     = "2"
  kubernetes_version = module.cluster.kubernetes_version
}

