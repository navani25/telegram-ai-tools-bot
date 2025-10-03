from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8436114041:AAGVRdbnsZMTCVf1tWlIflLBLeJutA-sF-8"

# AI Tools organized by category
AI_TOOLS = {
    "🧠 AI Assistants & Chatbots": [
        ("ChatGPT", "https://chat.openai.com/"),
        ("Claude", "https://www.anthropic.com/"),
        ("Jasper", "https://www.jasper.ai/"),
        ("Copy.ai", "https://www.copy.ai/"),
        ("Rytr", "https://rytr.me/"),
        ("Notion AI", "https://www.notion.so/product/ai"),
        ("Google Gemini", "https://gemini.google/"),
        ("Perplexity AI", "https://www.perplexity.ai/"),
        ("Bard", "https://bard.google.com/"),
        ("YouChat", "https://you.com/youchat")
    ],
    "✍️ Writing & Content Creation": [
        ("Grammarly", "https://www.grammarly.com/"),
        ("QuillBot", "https://quillbot.com/"),
        ("INK Editor", "https://inkforall.com/"),
        ("WriteSonic", "https://writesonic.com/"),
        ("ContentBot", "https://contentbot.ai/"),
        ("Scalenut", "https://www.scalenut.com/"),
        ("Scribe", "https://scribehow.com/"),
        ("Simplified", "https://simplified.com/"),
        ("Peppertype", "https://www.peppertype.ai/"),
        ("Frase", "https://www.frase.io/")
    ],
    "🎨 Design & Creativity": [
        ("Canva", "https://www.canva.com/"),
        ("Fotor", "https://www.fotor.com/"),
        ("Crello", "https://crello.com/"),
        ("Lumen5", "https://lumen5.com/"),
        ("Piktochart", "https://piktochart.com/"),
        ("Visme", "https://www.visme.co/"),
        ("Animoto", "https://animoto.com/"),
        ("Snappa", "https://snappa.com/"),
        ("Stencil", "https://getstencil.com/"),
        ("RelayThat", "https://relaythat.com/")
    ],
    "🖼️ Image Generation & Editing": [
        ("DALL·E", "https://openai.com/dall-e"),
        ("Midjourney", "https://www.midjourney.com/"),
        ("Deep Dream Generator", "https://deepdreamgenerator.com/"),
        ("Artbreeder", "https://www.artbreeder.com/"),
        ("Runway ML", "https://runwayml.com/"),
        ("NightCafe", "https://creator.nightcafe.studio/"),
        ("StarryAI", "https://www.starryai.com/"),
        ("Fotor AI", "https://www.fotor.com/features/ai-image-generator/"),
        ("DeepAI", "https://deepai.org/machine-learning-model/text2img"),
        ("BigSleep", "https://github.com/lucidrains/big-sleep")
    ],
    "🎥 Video Creation & Editing": [
        ("Synthesia", "https://www.synthesia.io/"),
        ("Pictory", "https://pictory.ai/"),
        ("InVideo", "https://invideo.io/"),
        ("Kapwing", "https://www.kapwing.com/"),
        ("Magisto", "https://www.magisto.com/"),
        ("Clipchamp", "https://www.clipchamp.com/"),
        ("WeVideo", "https://www.wevideo.com/"),
        ("Adobe Spark", "https://spark.adobe.com/"),
        ("FlexClip", "https://www.flexclip.com/"),
        ("Animoto", "https://animoto.com/")
    ],
    "🧪 Research & Education": [
        ("Google Scholar", "https://scholar.google.com/"),
        ("Zotero", "https://www.zotero.org/"),
        ("Mendeley", "https://www.mendeley.com/"),
        ("EndNote", "https://endnote.com/"),
        ("RefWorks", "https://www.refworks.com/"),
        ("Overleaf", "https://www.overleaf.com/"),
        ("Khan Academy", "https://www.khanacademy.org/"),
        ("Coursera", "https://www.coursera.org/"),
        ("edX", "https://www.edx.org/"),
        ("Duolingo", "https://www.duolingo.com/")
    ],
    "📊 Data Analysis & Visualization": [
        ("Google Data Studio", "https://datastudio.google.com/"),
        ("Tableau Public", "https://public.tableau.com/"),
        ("Power BI", "https://powerbi.microsoft.com/"),
        ("Plotly", "https://plotly.com/"),
        ("Datawrapper", "https://www.datawrapper.de/"),
        ("Zoho Analytics", "https://www.zoho.com/analytics/"),
        ("Qlik Sense", "https://www.qlik.com/us/products/qlik-sense"),
        ("Sisense", "https://www.sisense.com/"),
        ("Looker Studio", "https://lookerstudio.google.com/"),
        ("Google Sheets", "https://www.google.com/sheets/about/")
    ],
    "🛠️ Development & Automation": [
        ("GitHub Copilot", "https://github.com/features/copilot"),
        ("Replit", "https://replit.com/"),
        ("Glitch", "https://glitch.com/"),
        ("CodePen", "https://codepen.io/"),
        ("StackBlitz", "https://stackblitz.com/"),
        ("Vercel", "https://vercel.com/"),
        ("Netlify", "https://www.netlify.com/"),
        ("Zapier", "https://zapier.com/"),
        ("n8n", "https://n8n.io/"),
        ("Integromat", "https://www.make.com/")
    ],
    "🧩 Miscellaneous AI Tools": [
        ("Runway ML", "https://runwayml.com/"),
        ("DeepL Translator", "https://www.deepl.com/translator"),
        ("Otter.ai", "https://otter.ai/"),
        ("Descript", "https://www.descript.com/"),
        ("Sonix", "https://sonix.ai/"),
        ("Trint", "https://trint.com/"),
        ("Rev", "https://www.rev.com/"),
        ("Happy Scribe", "https://www.happyscribe.com/"),
        ("Speechify", "https://speechify.com/"),
        ("Tome", "https://tome.app/"),
        ("ChatSonic", "https://writesonic.com/chatsonic"),
        ("CopySmith", "https://copysmith.ai/"),
        ("CopyMonkey", "https://copymonkey.ai/"),
        ("ReimagineHome", "https://reimaginehome.ai/"),
        ("Looka", "https://looka.com/"),
        ("RunDiffusion", "https://rundiffusion.com/"),
        ("D-ID", "https://www.d-id.com/"),
        ("Soundraw", "https://soundraw.io/"),
        ("Cleanup.Pictures", "https://cleanup.pictures/"),
        ("Remove.bg", "https://www.remove.bg/")
    ]
}

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(cat, callback_data=cat)] for cat in AI_TOOLS.keys()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome! Choose a category to explore AI tools:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    category = query.data
    if category in AI_TOOLS:
        text = "\n".join([f"[{name}]({link})" for name, link in AI_TOOLS[category]])
        await query.edit_message_text(text=text, parse_mode='Markdown', disable_web_page_preview=True)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    print("Bot is running...")
    app.run_polling()