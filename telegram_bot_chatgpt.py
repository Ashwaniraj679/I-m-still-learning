import telegram
from telegram.ext import Updater, CommandHandler
import pafy
import urllib

# Replace TOKEN with your bot's token
updater = Updater(token='TOKEN', use_context=True)

def download_video(update, context):
    # Get the YouTube URL from the user's message
    youtube_url = update.message.text
    
    # Use pafy to get the video object
    video = pafy.new(youtube_url)
    
    # Choose the highest quality video
    best = video.getbest()
    
    # Download the video
    file_name = best.download()
    
    # Send the video to the user
    context.bot.send_document(chat_id=update.effective_chat.id, document=open(file_name, 'rb'))

# Set up the command handler for the /download command
download_handler = CommandHandler('download', download_video)
updater.dispatcher.add_handler(download_handler)

updater.start_polling()
