import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A8y5DajCf5E-5zmJwBZeuTQ0MKcFXV5M-D_AafIOt61fl7l4XAgyVk2c-c80sfy8mzePOXcx-MWd7MozjWriWlA96DJbi6M1xh6dgddDvUWUcIa1yCZE9UV2XNG7kcIyGrlT-IySxenA'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload to dropbox: ")

    transferData.upload_file(file_from, file_to)
    print("file has been uploaded to dropbox")

if __name__ == '__main__':
    main()