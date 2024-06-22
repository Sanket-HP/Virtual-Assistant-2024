# 🖥️ Desktop Assistant with GUI

Welcome to the Desktop Assistant project! This Python application leverages speech recognition, text-to-speech, and a simple graphical user interface to assist you with various tasks. 🌟

## 📋 Features

- **Speech Recognition** 🎤: Understands and processes voice commands.
- **Text-to-Speech** 🗣️: Responds to commands verbally.
- **Time and Day Information** ⏰: Tells you the current time and day.
- **Web Browsing** 🌐: Opens popular websites like Google and GeeksforGeeks.
- **Wikipedia Search** 📚: Retrieves summaries from Wikipedia.
- **Graphical User Interface** 🖼️: Simple GUI for interacting with the assistant.

## 🛠️ Installation

To run this project, you'll need to have Python installed on your machine along with a few libraries. Here's how you can set it up:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/desktop-assistant.git
   cd desktop-assistant
   ```

2. **Install dependencies**:
   ```sh
   pip install pyttsx3 SpeechRecognition wikipedia tk
   ```

3. **Run the script**:
   ```sh
   python your_script_name.py
   ```

## 🚀 How to Use

### Voice Commands

The assistant can handle several voice commands. Here are some examples:

- **Greet the Assistant**:
  ```
  Hello
  ```
  Response: "Hello sir I am your desktop assistant Jearry. Tell me how may I help you"

- **Open Websites**:
  ```
  Open Google
  Open GeeksforGeeks
  ```

- **Get Time and Day**:
  ```
  Tell me the time
  Which day it is
  ```

- **Search Wikipedia**:
  ```
  Tell me about Python from Wikipedia
  ```

- **Exit the Assistant**:
  ```
  Bye
  ```

### GUI Commands

The GUI provides buttons to open websites and search Wikipedia directly.

1. **Open GeeksforGeeks**: Click the "Open GeeksforGeeks" button.
2. **Open Google**: Click the "Open Google" button.
3. **Search Wikipedia**:
   - Enter the search term in the text field.
   - Click the "Search Wikipedia" button.

## 👨‍💻 Code Structure

- `takeCommand()`: Listens for voice commands.
- `speak(audio)`: Converts text to speech.
- `tellDay()`: Tells the current day.
- `tellTime()`: Tells the current time.
- `Hello()`: Greets the user.
- `openGeeksForGeeks()`: Opens GeeksforGeeks website.
- `openGoogle()`: Opens Google website.
- `searchWikipedia(query)`: Searches Wikipedia and speaks the summary.
- `create_gui()`: Creates the GUI for the assistant.
- `Take_query()`: Main function to handle voice commands.

## 🌟 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the MIT License.
