from db import get_session
from model import User_info, MALL
import discord

def get_profile(user_id):

    session = get_session()

    user_query = session.query(User_info).filter(User_info.user_id == str(user_id)).first()

    print(user_query)
    embed = discord.Embed(
            title="🧑‍💻 Welcome to your profile",
            color=0xe6e6e6
        )
    embed.add_field(name=f"> ***Name*** 🎁: ```{user_query.name} ```   ***Title*** 💼: ```{user_query.title}``` , ***Department*** 📠: ```{user_query.department}```",
                        value="Hello, my name is carl. I am an IT engineer with 7 years of experience in the field. I have a strong background in python language, and I am highly skilled in troubleshooting and problem solving.\n\n I am proficient in CI/CD, and have worked on several projects, ranging from developing applications to implementing and maintaining large-scale IT systems. I am always eager to learn and stay up to date with the latest advancements in technology.", inline=False)
    embed.add_field(name=f"> ***Points*** 💰: ```{user_query.points} ```", value="", inline=False)
    return embed

def check_wallet(user_id, commodity_points) -> bool:

    session = get_session()
    user_query = session.query(User_info).filter(User_info.user_id == str(user_id)).first()
    print(user_query.points)
    if int(str(user_query.points)) < int(str(commodity_points)):
        return False
    else:
        return True

def purchase(user_id, commodity, commodity_points):

    session = get_session()
    user_query = session.query(User_info).filter(User_info.user_id == str(user_id)).first()
    points = int(str(user_query.points))
    points -= int(str(commodity_points))

    USER_DATA = []

    USER_DATA = User_info(
        name=str(user_query.points),
        user_id=str(user_query.user_id),
        points=points
    )

    session.merge(USER_DATA)
    session.commit()

    mall_query = session.query(MALL).filter(MALL.commodity.ilike(
        f"%{commodity}%")).first()

    amount = int(mall_query.amount)
    amount -= 1
    MALL_DATA = []

    MALL_DATA = MALL(
        commodity=str(mall_query.commodity),
        points=str(mall_query.points),
        amount=str(amount)
    )

    session.merge(MALL_DATA)
    session.commit()


def get_mall_embeds():

    embeds = []
    session = get_session()

    product_query = session.query(MALL).all()

    for object in product_query:

        embed = discord.Embed(
            title="🌲 Welcome to Discord MALL",
            description="🚀 Go shop, Go pay !!! ",
            color=0xe6e6e6
        )

        embed.set_image(
            url=f"{object.image_url}"
        )

        embed.add_field(name=f"> ***Commodity*** 🎁: ```{object.commodity} ```   ***Point*** 💰: ```{object.points}``` , ***Number***: ```{object.amount}```",
                        value=str(object.description), inline=False)
        # embed.add_field(name=f"{product_dict['movie ticket'][0]} 🎁 Point: ```{product_dict['movie ticket'][1]}``` , Number: ```{product_dict['movie ticket'][2]}```", value="The list command only operates within the current directory and does not display information for items in subdirectories.\u200B \n Displays a list of all items, including hidden items, in the current directory", inline=False)

        embeds.append(embed)

    print(embeds)

    return embeds

async def insert_user_info(user, user_id, title, department):

    session = get_session()

    USERINFO_DATA = []

    USERINFO_DATA = User_info(
        name=str(user),
        user_id=str(user_id),
        title=str(title),
        department=str(department),
    )

    session.merge(USERINFO_DATA)
    session.commit()