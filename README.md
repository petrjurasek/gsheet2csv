# Google sheet to csv

## Usage

* create credentials file, default name is
```
credentials.json
```

* setup share on doc

```
python3 main.py --sheet_key "key_of_sheet" --worksheet "name_of_worksheet"
```

using different credentials file

```
python3 main.py --sheet_key "key_of_sheet" --worksheet "name_of_worksheet" --credentials "/path/to/credentials.json"
```

### Docker image

#### Build docker image

```
docker build -t petrjurasek/gsheet2csv .
```

#### Use image
```
docker run --rm -v $PWD/credentials.json:/app/credentials.json petrjurasek/gsheet2csv  --sheet_key "name_of_worksheet" --worksheet "name_of_worksheet"
```

## Dev

run
```
pipenv run pip install -r <(pipenv lock -r) --target vendor
```
to install dependencies
