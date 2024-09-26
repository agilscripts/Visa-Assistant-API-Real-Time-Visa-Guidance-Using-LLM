# Overview

This project is a Flask-based web application that acts as a visa assistant. The application uses OpenAI’s GPT model to answer visa-related questions in real-time. The assistant provides guidance on visa application processes and travel-related queries. Users simply input their question, and the assistant responds with detailed information.


<img width="777" alt="Screenshot 2024-09-26 at 2 46 56 AM" src="https://github.com/user-attachments/assets/991a726a-0de3-4ab9-8f7b-01dd38bccdab">



## Key Features

- **Real-time Visa Assistance**: Users ask visa-related questions, and the assistant provides clear, concise answers based on their inquiries.
- **Flask Backend**: The backend is built using Flask, handling API requests and interacting with OpenAI's API for generating responses.
- **Simple UI**: A straightforward HTML/CSS front-end with a chat-style interface, allowing users to ask questions and receive responses.

## Technologies Used

- **Flask**: For backend API development.
- **OpenAI GPT**: For generating dynamic responses to user inquiries.
- **HTML/CSS/JavaScript**: For the front-end chat interface.

## How to Set Up

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/VisaAssistantAPI.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd VisaAssistantAPI
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    - Create a `.env` file in the root directory and add your OpenAI API key:
      ```bash
      OPENAI_API_KEY=your_openai_api_key
      ```

5. **Run the application**:
    ```bash
    python main.py
    ```

6. **Access the application**:
    Open your browser and go to `http://127.0.0.1:5000`.

## API Endpoints

### `POST /ask`
- **Request** (JSON):
    ```json
    {
      "question": "How do I apply for a visa?"
    }
    ```

- **Response** (JSON):
    ```json
    {
      "response": "To apply for a visa, you need to..."
    }
    ```


### Future Enhancements:
- **Database Integration**: To track user queries.
- **Cloud Deployment**: Deploy the application to cloud platforms (AWS, Azure, GCP) for scalability.
- **User Authentication**: For personalized visa guidance.
- **Advanced Analytics**: To measure response accuracy and enhance user experience
