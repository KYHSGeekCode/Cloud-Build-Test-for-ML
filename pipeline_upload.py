from google.cloud import storage
import google.auth

if __name__ == "__main__":
    credentials, project_id = google.auth.default()
    
    REGION = "us-central1"
    BUCKET_NAME="gs://" + project_id + "-vertexai"
    DISPLAY_NAME="damagedcar"
    PIPELINE_NAME=DISPLAY_NAME + "-pipeline"

    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME.replace("gs://", ""))
    blob = bucket.blob(PIPELINE_NAME + ".json")
    blob.upload_from_filename(PIPELINE_NAME + ".json")
