# Introduction:
Rasa is an open-source conversational AI framework that allows developers to build chatbots and voice assistants for various use cases. This document provides instructions on how to install Rasa and use it to train and run a chatbot application.

# Prerequisites:
Before installing Rasa, make sure that your pip version is up to date. You can update pip by running the following command:

`pip install --upgrade pip`

# Installation:
To install Rasa, run the following command in the terminal:

`pip3 install rasa`

# Training:
To train your Rasa chatbot, navigate to your chatbot project directory and run the following command:

`rasa train`

# Running the App:
Before running the Rasa shell, you must first run the action server. To do so, navigate to your project directory and run the following command:
`rasa run actions`

In a new terminal run the Rasa shell, by running the following command in the terminal:

`rasa shell`

# API Integration:
In addition to running Rasa on the terminal, you can also run it on Postman by using the following command:

`rasa run --enable-api`

# Conclusion:
In this document, you learned how to install Rasa and use it to train and run a chatbot application. You also learned how to run Rasa on Postman. For more detailed documentation, visit the official Rasa website.
