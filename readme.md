
---

# MIND HELP BOT

**MIND HELP BOT** is a Telegram bot designed to provide psychological support, prevent suicidal behavior and self-harm, and promote mental health well-being. The bot uses artificial intelligence to assist users in crisis situations, offering both text-based and voice-based support.

## Features

- **Mental Health Support**: The bot assists users in managing negative emotions, stress, and mental health challenges through guided conversations and resources.
- **Suicide and Self-Harm Prevention**: Built-in algorithms help identify at-risk users and provide immediate intervention or support.
- **Text-to-Speech (TTS) Responses**: The bot uses Google Text-to-Speech (gTTS) to convert supportive messages into voice responses for users.
- **AI-Powered Conversations**: With the integration of the OpenAI API, the bot is capable of offering empathetic and tailored conversations, making the interaction feel more human.

## Tech Stack

- **Python**: Main programming language used to develop the bot.
  - **Aiogram**: A lightweight Telegram framework used to handle bot functionality.
  - **gTTS (Google Text-to-Speech)**: Converts text-based messages into voice format for users who prefer listening.
- **Figma**: Used for designing UI/UX mockups and prototyping the bot’s flow and structure.
- **OpenAI API**: Powers the AI-drien conversations, providing empathetic and context-aware responses to users.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/MIND_HELP_BOT.git
    cd MIND_HELP_BOT
    ```

2. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your environment variables:
    - Create a `.env` file with the following variables:
        - `TELEGRAM_TOKEN`: Your Telegram Bot API token.
        - `OPENAI_API_KEY`: Your OpenAI API key.
  
    Example:
    ```env
    TELEGRAM_TOKEN=your-telegram-token
    OPENAI_API_KEY=your-openai-key
    ```

4. Run the bot:

    ```bash
    python bot.py
    ```

## Usage

1. Open Telegram and find your bot using the bot username.
2. Start the conversation with `/start`.
3. The bot will offer guided support to address mental health concerns.
4. You can request voice responses using the `/voice` command.

## Key Files

- `bot.py`: The main bot logic and event handling.
- `conversation_handler.py`: Handles different conversation flows and interactions with the user.
- `gtts_handler.py`: Converts text responses into voice using Google Text-to-Speech.
- `openai_handler.py`: Manages the OpenAI API calls for AI-generated responses.
- `design/`: Contains Figma design files and mockups.

## Contributing

Contributions are welcome! Please fork the repository, create a new branch for your features or bug fixes, and submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
