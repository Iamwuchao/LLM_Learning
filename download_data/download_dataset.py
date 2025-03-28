from datasets import load_dataset

ds = load_dataset("parquet",
                  data_files={
                      'train':"/Users/bigo/PycharmProjects/pythonProject/LLM_test/data_set/synthetic_text_to_sql_train.snappy.parquet",
                      'test' : '/Users/bigo/PycharmProjects/pythonProject/LLM_test/data_set/synthetic_text_to_sql_test.snappy.parquet'
                  }
                  )
training_ds = ds["train"]

valid_ds = ds["test"]