import os
import subprocess


class fs_base(object):

    def sorted_ls(self, path):
        mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
        return list(sorted(os.listdir(path), key=mtime))
    
    
    def scp_iphone(self, source, destination):
        process = subprocess.Popen("scp -r root@ruisiphone:%s %s" % (source, destination), shell=True,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output,stderr = process.communicate()
        status = process.poll()
    #    print output
        return output
    
    
    def get_latest_repo(self, repos):
        return repos.split('\n')[0]
    
    
    def cap_latest_data(self, path, repo):
        file_list = [name for name in os.listdir("%s/%s/Documents" % (path, repo))]
        file_list.sort(reverse=True)
        return file_list[0]
    
    
    def find_data_container(self, path, key):
        data_repo = None
        for repo in os.listdir(path):
            metafile = "%s/%s/.com.apple.mobile_container_manager.metadata.plist" % (path, repo)
            if os.path.exists(metafile):
                with open(metafile, 'r') as fp:
                    if key in fp.read():
                        data_repo = "%s/%s" % (path, repo)
                        break
        return data_repo
    
    
    def cap_latest_tagging_file(self, data_repo):
        tagging_file_list = os.listdir("%s/Documents" % data_repo)
        tagging_file_list.sort(reverse=True)
        return "%s/Documents/%s" % (data_repo, tagging_file_list[0])
