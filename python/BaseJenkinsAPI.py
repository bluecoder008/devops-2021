#!/usr/bin/env python3
import jenkinsapi
import sys

from jenkinsapi.jenkins import Jenkins


class BaseJenkinsAPI:

    def __init__(self, server_url, username=None, password=None):
        self.url = server_url
        self.username = username
        self.password = password
        if self.username and self.password:
            self.instance = Jenkins(self.url, self.username, self.password)
        else:
            self.instance = Jenkins(self.url)

    def get_name(self):
        return self.url

    def get_version(self):
        return self.instance.version

    def get_api_version(self):
        return jenkinsapi.__version__

    def get_number_jobs(self):
        return len(self.instance.keys())


# test driver
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("BaseJenkinsAPI.py <url> <username> <password>\n")
        sys.exit(-1)
    base_jenkins = BaseJenkinsAPI(sys.argv[1], sys.argv[2], sys.argv[3])
    print('There are %d jenkins jobs on Jenkins server %s (on version %s and api version %s)'
          % (base_jenkins.get_number_jobs(), base_jenkins.get_name(),
             base_jenkins.get_version(), base_jenkins.get_api_version()))
