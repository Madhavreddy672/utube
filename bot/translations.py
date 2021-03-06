
class Messages:

    START_MSG = "Hi {}.\n\nI'm Youtube Uploader Bot.You can use me to upload any telegram video to youtube once you authorise me. You can know more from /help.\n\nTelegram Group: @linux_repo \nTelegram Channel: @Discovery_Updates"

    HELP_MSG = [
        ".",
        "Hi there.\n\nFirst things first. You should be aware that youtube processes each and every video uploaded, and it's AI is amazing that it flags the video for copyrights if it finds copywrited content as soon as its uploaded, and you will not be able to publish the video.\n\nRead through all the pages to know how I work.",

        "**Lets learn how I work.**\n\n**Step 1:** __You [authorise](https://accounts.google.com/o/oauth2/v2/auth?client_id=905188182711-vnh37gt314tqvhgaftgbm9aambp36bsm.apps.googleusercontent.com&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fyoutube.upload&access_type=offline&response_type=code) me to upload to your youtube channel. More about this in comming pages.__\n\n**Step 2:** __You forward any Telegram video to me.__\n\n**Step 3:** __You reply __/upload __to the forwarded video file. You can also specify some title in the upload command, but its optional though. Title will follow the __`/upload`. __If no title is given, filename will be used as title.__\n\n**Step 4:** I remotely download the file and uploads to your Youtube channel.\n\n**Step 5:** I send you the Youtube link after upload.",

        "**Create your YouTube Channel**\n\nThere is no point in using me if you don't have a Youtube Channel. So go through the given steps to create one.\n\n**Step 1:** __Sign in to YouTube on a computer or using the mobile.__\n\n**Step 2:** __Try any action that requires a channel, such as uploading a video, posting a comment, or creating a playlist.__\n\n**Step 3:** __If you don't yet have a channel, you'll see a prompt to create a channel.__\n\n**Step 4:** __Check the details and confirm to create your new channel.__",

        "**Verify your YouTube account**\n\nYouTube take spam and abuse very seriously. So you are asked to verify your Youtube account. Once you've verified your account, you will be able to upload videos longer than 15 minutes. If you haven't verified your account every video uploaded which are longer than 15 minutes will be removed.\n\n[Verify your Youtube account](http://www.youtube.com/verify)\n\n__Remember to verify your project, else your uploads will be kept private.__",

        "**Now lets authorise.**\n\nYou need to give me the access to upload videos to your Youtube account.For that open the given link and allow access and copy the code. Come back here and type `/authorise copied-code` and send it.\n\n**Fear not!**\nI'm not a hacker or someone who wants to creep into people's privacy. I respect one's privacy. I'm here just to help anyone who wants help. If I was a hacker I won't be sitting here writing Telegram Bots. \n\nTalk with us on Telegram Group: [Linux Repositories](http://t.me/linux_repo)"
    ]

    NOT_A_REPLY_MSG = "Please reply to some video file."

    NOT_A_MEDIA_MSG = "No media file found. "+NOT_A_REPLY_MSG

    NOT_A_VALID_MEDIA_MSG = "This is not a valid media"
    
    DAILY_QOUTA_REACHED = "Looks like you are trying to upload more than 6 videos today! By default youtube only allows about 6 uploads daily, so this request might fail!!"

    PROCESSING = "Processing ..."

    NOT_AUTHENTICATED_MSG = "You have not authenticated me to upload video to any account. see /help to authenticate."

    NO_AUTH_CODE_MSG = "There is no code. Please provide some code."

    AUTH_SUCCESS_MSG = "Congrats, you have successfully authenticated me to upload to Youtube.\nHappy uploading!"

    AUTH_FAILED_MSG = "Authentication failed\nDetails:{}"
    
    AUTH_DATA_SAVE_SUCCESS = "Successfully saved the given auth data!"
    
