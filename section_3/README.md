# Pros
- Store use S3. With technology improving, image quality are getting better along with the size
  - Cheap object storage with high up-time guarantee by AWS
- Use Flink as State Streaming Processing engine
  - Low latency for BI tools
  - Fault tolerant
  - Built in state management mechanism

# Cons
- S3 is not atomic. Need to ensure image is successfully uploaded before sending event