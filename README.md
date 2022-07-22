## Musical

- A Single View application aggregates and reconciles data from multiple sources to create a single view of an entity.
- The data is read from a csv file and inserted into a postgresql database.
- A single enpoint exists to view a musical work by it's _iswc_.

## Getting started

- Clone this repository
- Run the following commands in order (Ensure you have docker installed)

```
docker-compose build

docker-compose up

docker exec -it musicals python manage.py migrate
```

## Creating musical works

- Run the `createmusicals` django command to create musical works from the sample csv file as shown below.
- `docker exec -it musicals python manage.py createmusicals test_csvs/works_metadata.csv`

## Testing

- Run `python manage.py test`

#### The endpoint

- Visit `http://localhost:8000/api/musicals/T0101974597/` to view a musical picked by it's iswc.
- You can check `./test_csvs/csv.csv` directory to pick an _iswc_ and test the endpoint.
