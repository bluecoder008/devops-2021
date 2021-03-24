#!/usr/bin/env python3

from __future__ import print_function

from BaseJenkinsAPI import BaseJenkinsAPI
import sys

from jenkinsapi.job import Job
from jenkinsapi.custom_exceptions import JenkinsAPIException

# in python3, no reason to inherit from object class


class BaseJenkinsJob:

    def __init__(self, server, name):
        self._server = server
        self._name = name
        # if self._server.has_job(name):
        #     print("The job {} is already in server.".format(name))
        for job_name, job_instance in server.get_jobs():
            # print('Job Name:%s' % (job_instance.name))
            # print('\tJob Description:%s' % (job_instance.get_description()))
            # print('\tIs Job running:%s' % (job_instance.is_running()))
            # print('\tIs Job enabled:%s' % (job_instance.is_enabled()))
            # print('\tJob config xml:%s' % (job_instance.get_config()))
            if job_name == name:
                self._config_xml = job_instance.get_config()

    def get_config_xml(self):
        return self._config_xml if self._config_xml else None

    def copy_job(self, job_name, new_job_name):
        self._server.copy_job(job_name, new_job_name)
    #
    # def create(self, config_xml):
    #     """
    #     Create a job
    #     :param str config_xml: XML configuration of new job
    #     """
    #     if not config_xml:
    #         raise JenkinsAPIException('Job XML config cannot be empty')
    #
    #     params = {'name': self._name}
    #     self._server.get_requester().post_xml_and_confirm_status(
    #         self._server.get_create_url(),
    #         data=config_xml,
    #         params=params
    #     )
    #     print("The job {} has been successfully created".format(self._name))


# test driver
if __name__ == "__main__":
    if len(sys.argv) < 5:
        sys.exit("BaseJenkinsJob.py <url> <username> <password> <job-name> "
                 "[--clone | --create | --trigger]\n")
    url = sys.argv[1]
    base_jenkins = BaseJenkinsAPI(url, sys.argv[2], sys.argv[3])
    job_name = sys.argv[4]
    op = sys.argv[5] if len(sys.argv) >= 6 else None

    if op and op == "--clone":
        """
           python3 -m BaseJenkinsJob http://localhost:8080 admin \
                `cat jenkins-api-token.txt` git_webhook_demo --clone
        """
        if not base_jenkins.has_job(job_name):
            sys.exit("Job {} is not a valid job name on server {}"
                     .format(job_name, url))
        new_job = input("Please give the new job name to clone from job {} : "
                        .format(job_name))
        if base_jenkins.has_job(new_job):
            sys.exit("Job name '{}' already present in the Jenkins server, "
                     "please choose a different job name."
                     .format(new_job))
        try:
            base_jenkins_job = BaseJenkinsJob(base_jenkins, job_name)
            base_jenkins_job.copy_job(job_name, new_job)
        except JenkinsAPIException as je:
            print("caught exception: {}".format(je))
        print("Successfully cloned job from {}: {}".format(job_name, new_job))

    elif op and op == "--create":
        """
           python3 -m BaseJenkinsJob http://localhost:8080 admin \
                `cat jenkins-api-token.txt` git_webhook_demo-new --create config.xml
        """
        if base_jenkins.has_job(job_name):
            sys.exit("Job {} is already present on server {}, use a different name."
                     .format(job_name, url))
        if len(sys.argv) < 7:
            sys.exit("Missing input config xml file for JJ create.")

        with open(sys.argv[6], "r") as input_file:
            config_xml = input_file.read()

        base_jenkins_job = base_jenkins.create_job(job_name, config_xml)

    elif op and op == "--trigger":
        """
           python3 -m BaseJenkinsJob http://localhost:8080 admin \
                `cat jenkins-api-token.txt` git_webhook_demo --trigger
        """
        base_jenkins.build_job(job_name)

    else:
        """
           python3 -m BaseJenkinsJob http://localhost:8080 admin \
                  `cat jenkins-api-token.txt` git_webhook_demo config.xml
        """
        base_jenkins_job = BaseJenkinsJob(base_jenkins, job_name)
        config_xml = base_jenkins_job.get_config_xml()
        if op:
            out_file = op
            with open(out_file, 'w') as output_file:
                output_file.write(config_xml)
            print("Job config xml written to '{}'".format(out_file))
        else:
            print("Job config xml:\n{}".format(config_xml))
