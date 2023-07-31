# Docker Compose and Mongo

This week I have implemented a docker-compose.yml to begin defining our
deployment. I have made some overall changes to begin structuring our app
to store weather data and reports in a Mongo database, from which
we will eventually display weather statistics as well as provide a
Prometheus metrics exporter

## Your task

Run the following to test the new tool:
	- `docker compose build`
	- `docker compose up`

* In your NOTES.md, add the following notes:
	* Explain what docker-compose.yml does
	* Explain each main part of the configuration I have placed in docker-compose.yml
	* Read through the updates I made to frontend.py and explain what the code does

Now, complete the following tasks in the code:
	- Create a main weather update loop that runs every UPDATE_INTERVAL seconds
		- UPDATE_INTERVAL should be set by environment (in your docker-compose.yml)
		- WEATHER_LOCATION should also be set by environment and should give you enough to
			determine what weather date you will be collecting. It could be a zip/postal code e.g. 46725
		- Retrieve some weather data from any weather API
		- Format some statistics (e.g. current conditions) in a json structure you define
			- A json schema would be nice but at minimum document the fields
		- Store the data in a mongo collection in the database I have connected to for you
	- Add an endpoint to your http server at /weather that returns current conditions as well
		as avg, min, and max temperature and barometric pressure over the past 24 hours

When you are done, push your code to this branch and create a PR with a detailed note. Assign it to me.
