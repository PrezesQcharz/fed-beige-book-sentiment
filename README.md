# FED Beige Book Sentiment Analysis

Fetches the latest Beige Book, runs sentiment analysis with ChatGPT, and emails you the result.

**How to use:**

1. Build the Docker image:

    docker build -t fed-beige-book-sentiment .

2. Run the program (replace values with your own):

    docker run --rm ^
      -e OPENAI_API_KEY=sk-xxxxxxxx ^
      -e EMAIL_HOST=smtp.gmail.com ^
      -e EMAIL_PORT=465 ^
      -e EMAIL_HOST_USER=your@email.com ^
      -e EMAIL_HOST_PASSWORD=yourapppassword ^
      -e RECIPIENTS=your@email.com ^
      fed-beige-book-sentiment

No credentials or API keys are stored in the code or git history.
