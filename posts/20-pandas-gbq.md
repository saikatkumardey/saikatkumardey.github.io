---
date: 2024-03-15
title: Access BQ from Python
postSlug: access-bq-from-a-python
featured: false
ogImage: ""
categories:
  - python
  - bq
description: How to access BQ from Python?
---

You need to install pandas-gbq first.

```
pip install pandas-gbq
```



## If you're using Google Colab

It's easy. Authenticate to all Google cloud services your user-account has access to in this way:

```
from google.colab import auth
auth.authenticate_user()
```

Once that's done, run your query from pandas-gbq.

```
import pandas as pd
PROJECT_ID = ""
df = pd.read_gbq(query,project_id=PROJECT_ID)
```


## If you're using a VM

### Using Service Account

Follow the steps [here](https://cloud.google.com/iam/docs/service-accounts-create) to create a service account.

```
from google.oauth2 import service_account
import pandas_gbq

credentials = service_account.Credentials.from_service_account_file(
    'path/to/key.json',
)
df = pandas_gbq.read_gbq(sql, project_id="YOUR-PROJECT-ID", credentials=credentials)
```


### Using a user-account

Install the gcloud CLI from [here](https://cloud.google.com/sdk/docs/install).

Run the following to authenticate your user account.
```
gcloud auth login
```

You need to install `pydata_google_auth` as well.

```
pip install pydata-google-auth
```

Then you can access BQ from your notebook or script in this way:

```
import pandas_gbq
import pydata_google_auth
credentials, project = pydata_google_auth.default()
PROJECT_ID = ""

df = pd.read_gbq(query,project_id = PROJECT_ID, credentials = credentials)
```
