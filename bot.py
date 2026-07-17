from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 به سامانه ثبت‌نام سرویس VPN خوش آمدید.\n\n"
        "🎁 تست رایگان ۱ گیگابایتی برای کاربران جدید فعال است.\n\n"
        "📱 جهت ادامه، لطفاً شماره تماس خود را از طریق دکمه زیر ارسال نمایید."
    )
