import os
import asyncio
import nest_asyncio
nest_asyncio.apply()
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = 'TELEGRAM_TOKEN'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Hello! Welcome to Kaycee\'s store!')

# Define the main function to start the bot
async def main() -> None:
    """Start the bot."""
    from asyncio import get_event_loop  # Import get_event_loop
    token = os.environ.get('TELEGRAM_TOKEN')
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # Register the /start command handler
    application.add_handler(CommandHandler("start", start_command))

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    await application.run_polling()

    # Gracefully stop the event loop before exiting
    loop = get_event_loop()  # Get the event loop
    await asyncio.gather(
        application.stop(),  # Stop the Telegram bot application
        loop.shutdown_asyncgens(),  # Shutdown any async generators
    )

if __name__ == '__main__':
    asyncio.run(main())
