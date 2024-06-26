# text_summarization_fastapi

This application provides a simple API for summarizing text.

Install the required dependencies using the following command:
    
    pip install -r requirements.txt

How to Run the Application

Option 1: Running via main.py and using curl for testing

Execute main.py to start the FastAPI server:
    
    python main.py
    
or
    
    uvicorn main:app --reload

The server will start at http://127.0.0.1:8000.

Testing the API using curl:

Open a new terminal window and run the following curl command to send a POST request with JSON data for summarization:

        curl -X POST http://127.0.0.1:8000/summarize \
    -H "Content-Type: application/json" \
    -d '{"text": "The Roman Empire is generally understood to mean the period and territory ruled by the Romans following Octavian assumption of sole rule under the Principate in 27 BC, the post-Republican state of ancient Rome. It included territories in Europe, North Africa, and Western Asia and was ruled by emperors. The fall of the Western Roman Empire in 476 AD conventionally marks the end of classical antiquity and the beginning of the Middle Ages. By 100 BC, Rome had expanded its rule to most of the Mediterranean and beyond. However, it was severely destabilized by civil wars and political conflicts, which culminated in the victory of Octavian over Mark Antony and Cleopatra at the Battle of Actium in 31 BC, and the subsequent conquest of the Ptolemaic Kingdom in Egypt."}'


Replace the text inside d '{"text": ...}' with your own text for summarization.

Option 2: After running main.py, navigate to http://127.0.0.1:8000/docs, click on POST /summarize, and then click on "Try it out". In the request body, replace "string" with the text you want to summarize:

    {
      "text": "Your text goes here"
    }

Click "Execute", and you will see the summary in the Response section.

