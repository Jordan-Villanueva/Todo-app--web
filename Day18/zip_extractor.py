import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("/home/jortizvilla/PycharmProjects/For_Python_course/Day18/compressed.zip",
                    "/home/jortizvilla/PycharmProjects/For_Python_course/Day18")