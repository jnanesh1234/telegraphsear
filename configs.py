# (c) @RoyalKrrishna

import os
# from dotenv import load_dotenv

# load_dotenv()


class Config(object):
    API_ID = int(os.getenv("API_ID", "13271631"))
    API_HASH = os.getenv("API_HASH", "c53ac45c5e24205743c58ed8a748b90a")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "5316689662:AAEJEd2d0X6h5Bh6PXMQCsFKfPjUYvQUUmQ")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "MdiskSearchRobot")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "BQAB6uJ6mrsDsDpgKyMIA4ZEv1qAa0cWYaqbPZPz5ykU2pOMhT60GgiqFY_9IXAoiMmspPCdrbqOh-Nv96uFeBTqPMxvUOtbgpkZGQySblQ7OJjPKQZtrdz1phD63nfSmUMyLqOj0rZnfqcmHpGIx6Q6H60dtktasagSWum_PCI3rahXigAAI0yYdaLzFoetZdRb9W7RvZAYUWyiWBk5IAZ1QYaNppf60XdKcD9cByUKhHHWsubylnrge90I9xRomGPLT-qM_pyg4HfKQ15vqf-G-zLXP29S4Kt-Ji1GRX6jzCdg9wmd6W7Mpm2mXdSc5qqbHfUqgDCpwj_4Z9NGZYLKAAAAASzcR8gA")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", "-1001844452628"))
    BOT_USERNAME = os.getenv("BOT_USERNAME", "batchfilestorebot")
    BOT_OWNER = int(os.getenv("BOT_OWNER", "5047601096"))
#    OWNER_USERNAME = os.getenv("OWNER_USERNAME", "Beastonejnanesh")
    BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL", "ROCKERSBACKUP")
#    GROUP_USERNAME = os.getenv("GROUP_USERNAME")
    START_MSG = os.getenv("START_MSG", "Wait" )
    START_PHOTO = os.getenv("START_PHOTO", "https://telegra.ph/file/b57323ed245c34a374ac4.jpg")
    HOME_TEXT = os.getenv("HOME_TEXT", "Wait" )
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "ROCKERSBACKUP")
    DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://mangodb:mangodb@cluster0.dskkdky.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1001886911325"))
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", 20))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "ROCKERSBACKUP")
    FORCE_SUB = os.getenv("FORCE_SUB", "False")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 300))
    MDISK_API = os.getenv("MDISK_API", "nx7N3INpOrexpfSHYnp7")
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "31"))
    ABOUT_BOT_TEXT = os.getenv("ABOUT_TEXT", "Jald")
    ABOUT_HELP_TEXT = os.getenv("HELP_TEXT", "Soon" )
