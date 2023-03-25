from main import LoadData

load_data = LoadData()

def load_dataset_to_mongo_db():
    load_data.load_working_data()


def main():
    load_dataset_to_mongo_db()

if __name__ == "__main__":
    main()