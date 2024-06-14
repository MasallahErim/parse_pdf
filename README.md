## Getting Started ##
Make sure you have Docker and Docker Compose installed on your machine. You can follow the official installation guides:


- [Docker Installation](https://docs.docker.com/get-docker/)
- [Docker Compose Installation](https://docs.docker.com/compose/install/)


### Prerequisites ###


#Run Docker Compose:

```sh
docker-compose stop
```

This command will start the Flask web application and PostgreSQL database in separate containers.


### Usage ###

#Access the Application:
Open your web browser and go to http://localhost:8888/upload

#Upload a PDF:
Use the provided form to upload a PDF file. Once uploaded, the file will be saved in the designated directory and processed.

#Process the PDF:
After uploading the PDF, click the "Process Latest PDF" button to extract text from images in the PDF and save it to the database.

#View the Data:
Click the "View Data" button to display the extracted data in a table format.


###Stop the Services ###

#To stop the services:

```sh
docker-compose stop
```

## Repository and Setup

To get started with this project, clone the repository from GitHub and navigate to the project directory:

```sh
git clone https://github.com/MasallahErim/parse_pdf
cd parse_pdf
```

After navigating to the project directory, you can start the services by running:

```sh
docker-compose up
```

This will set up and run the web application and database services.

