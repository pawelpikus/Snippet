class FileManager(object):

    @staticmethod
    def read_file():
        file = 'snippet.txt'
        with open(file, 'r') as f:
            snippets_str = f.read()
            lbox_list = snippets_str.split('\n')
        return lbox_list

    @staticmethod
    def save_to_file(snippets_list):
        file = 'snippet.txt'
        with open(file, 'w') as f:
            f.write('\n'.join(snippets_list))
