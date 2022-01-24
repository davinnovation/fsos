# fsos

minio like python Local File System based Object Storage (FSOS)

## Usage

```
import fsos

fsos.make_bucket("my-bucket", ROOT_PATH)
fsos.remove_bucket("my-bucket", ROOT_PATH)
fsos.bucket_exists("my-bucket", ROOT_PATH)
fsos.list_buckets(ROOT_PATH)

fsos.list_objects("my-bucket", ROOT_PATH)

fsos.put_filepath("my-bucket", "my-image.png")
fsos.get_filepath("my-bucket", "my-image.png")
```

```
from fsos.utils import folder2bucket

folder2bucket("dir2bucket", FOLDER_PATH)
```
