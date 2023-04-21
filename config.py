from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "7452578")) #لا تغير هاذة القيمة
API_HASH = getenv("API_HASH", "061d67ee8eed9368c5cadabb4aa21efc")#لا تغير هاذة القيمة
BOT_TOKEN = getenv("BOT_TOKEN", "6287151927:AAHEX9NYzLeBqlHsdDd1Z1l3gqk-l1xIuMU")
SESSION_NAME  =  getenv ( "SESSION_NAME" ، "AgBUTYCItCevaC3Fw1Hn7noK2COQkkNQ-lJnCtghA0nmgt84xWB-yOeL-NCZoOxyD3Biw-O9ORFJ-RVi8ZftnslapC07Czmcr8e7PIP1CtuNCPr22vFnqwr_B8ZvdVrFe5ZoClhqDE8rhT8dIS3m2H0eRACRQ3b9o3AEP6Q5DhgQr7e-BM25DGyohparMkJmEkigenJXanKep3vvkmcZLOuye2W19ztBIP8FEBiGcMU0cL5r_idINZZp5GvA8XhYKS20zhGMcIreuxfcZiQSA3NJS5Nm8-EAxLOtFJzZTSqXqboE9iW6GUYN_FOKpqaqx-9iSel8kFhFBa1UiW1Q0Y6FAAAAAUyFnb4A" )

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "dr6_c") # @ هنا ضع يوزر حسابك بدون 
ALIVE_NAME = getenv("ALIVE_NAME", "𝒂𝒈𝒉𝒂𝒅 𝒎𝒖𝒔𝒊𝒄❥") # هنا ضع اسم حسابك
BOT_USERNAME = getenv("BOT_USERNAME", "mug7hhbot") # @ هنا ضع يوزر البوت بدون 
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/X02lx/RrRRR") 
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main") #لا تغير هاذة القيمة
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60")) #لا تغير هاذة القيمة
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "a_313_l_i_A1") # @ هنا ضغ يوزر كروبك بدون 
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "o511kk") # @ هنا ضغ يوزر قناتك بدون

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1854384004").split()))
                                             #هنا ضع ايدي المطور فوق و الاعلئ
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
