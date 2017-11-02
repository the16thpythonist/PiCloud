

class CloudHeartInterface:

    def __init__(self):
        pass

    def download(self, cloud_path):
        raise NotImplementedError()

    def upload(self, cloud_folder, local_path):
        raise NotImplementedError()

    def delete(self, cloud_path):
        raise NotImplementedError()

    def folder_exists(self, cloud_path):
        raise NotImplementedError()

    def file_exists(self, cloud_path):
        raise NotImplementedError()

    def path_tree(self):
        raise NotImplementedError()
