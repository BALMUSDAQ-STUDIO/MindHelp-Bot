![Logo](https://raw.githubusercontent.com/BALMUZDAQ-STUDIO/Balmuzdaq-logos/refs/heads/main/Balmuz_logo_1.png)

<h1 align="center">MIND HELP BOT</h1>

<img src="https://raw.githubusercontent.com/BALMUZDAQ-STUDIO/Balmuzdaq-logos/refs/heads/main/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-28%20%D0%B2%2019.24.10.png" alt="Alt text" width="400" align="right"/>

<span>MIND HELP BOT is a Telegram bot designed to provide psychological support,<br>
prevent suicidal behavior and self-harm, and promote mental health well-being. <br>
The bot uses artificial intelligence to assist users in crisis situations,
offering both <br> text-based and voice-based support.</span>

 **Features**

- **Mental Health Support**: The bot assists users in managing negative emotions, stress, and mental health challenges through guided conversations and resources.
- **Suicide and Self-Harm Prevention**: Built-in algorithms help identify at-risk users and provide immediate intervention or support.
- **Text-to-Speech (TTS) Responses**: The bot uses Google Text-to-Speech (gTTS) to convert supportive messages into voice responses for users.
- **AI-Powered Conversations**: With the integration of the OpenAI API, the bot offers empathetic and tailored conversations, making the interaction feel more human.

## Tech Stack

- **Python**: Main programming language used to develop the bot.
  - **Aiogram**: A lightweight Telegram framework used to handle bot functionality.
  - **gTTS (Google Text-to-Speech)**: Converts text-based messages into voice format for users who prefer listening.
- **Figma**: Used for designing UI/UX mockups and prototyping the bot's flow and structure.
- **OpenAI API**: Powers the AI-driven conversations, providing empathetic and context-aware responses to users.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/BALMUZDAQ-STUDIO/MindHelp-Bot.git
    cd MindHelp-Bot
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
    python main.py
    ```

## Usage

1. Open Telegram and find the bot using its username.
2. Start the conversation with `/start`.
3. The bot offers guided support to address mental health concerns.

## Key Files

- `main.py`: Main bot logic and event handling.
- `assets.py`: Static assets for the bot.

## Contributing

Contributions are welcome! Please fork the repository, create a new branch for your feature or bug fix, and submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## Authors

- [@maksimkaprosuperhacker](https://github.com/maksimkaprosuperhacker)

## Feedback

If you have any feedback, please reach out to us at balmuzdaq.studio@gmail.com

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
