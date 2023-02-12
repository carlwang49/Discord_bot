import discord
from db import get_session
from model import *


# Welcome Embed
def welcome_embed():

    embed = discord.Embed(
        title="🌲 Welcome to duty System ",
        color=0xe6e6e6
    )

    embed.add_field(name="We are committed to bringing together community leaders, moderators, designers, and developers to share our biggest passion: Building communities on Discord.🌱", value="\u200B", inline=False)
    embed.add_field(name="We offer several fantastic opportunities for experienced and new Discord users to share ideas, exchange advice, listen to informative stage events, receive feedback, collaborate, and create impactful communities.🌿", value="\u200B", inline=False)

    return embed


def welcome_timesheet_embed():

    embed = discord.Embed(
        title="🌲 Welcome to Timesheet System ",
        description="Please follow the rule below, hope you have fun experience 📃",
        color=0xe6e6e6
    )

    embed.add_field(name="We are committed to bringing together community leaders, moderators, designers, and developers to share our biggest passion: Building communities on Discord.🌱", value="\u200B", inline=False)
    # embed.add_field(name="We offer several fantastic opportunities for experienced and new Discord users to share ideas, exchange advice, listen to informative stage events, receive feedback, collaborate, and create impactful communities.🌿", value="\u200B", inline=False)

    return embed


def welcome_leave_embed():

    embed = discord.Embed(
        title="🍁 Welcome to Leave System ",
        description="Please follow the rule below, hope you have fun experience 📃",
        color=0xe6e6e6
    )

    embed.add_field(name="We are committed to bringing together community leaders, moderators, designers, and developers to share our biggest passion: Building communities on Discord.🌱", value="\u200B", inline=False)
    # embed.add_field(name="We offer several fantastic opportunities for experienced and new Discord users to share ideas, exchange advice, listen to informative stage events, receive feedback, collaborate, and create impactful communities.🌿", value="\u200B", inline=False)

    return embed


def welcome_overtime_embed():

    embed = discord.Embed(
        title="🔥 Welcome to Overtime System ",
        description="Please follow the rule below, hope you have fun experience 📃",
        color=0xe6e6e6
    )

    embed.add_field(name="We are committed to bringing together community leaders, moderators, designers, and developers to share our biggest passion: Building communities on Discord.🌱", value="\u200B", inline=False)
    # embed.add_field(name="We offer several fantastic opportunities for experienced and new Discord users to share ideas, exchange advice, listen to informative stage events, receive feedback, collaborate, and create impactful communities.🌿", value="\u200B", inline=False)

    return embed

# still in development Embed

def still_in_develop_embed():

    embed = discord.Embed(
        title="⛏ Sorry...still in development... ",
        color=0xe6e6e6
    )

    embed.add_field(name="We are committed to bringing together community leaders, moderators, designers, and developers to share our biggest passion: Building communities on Discord.🌱", value="\u200B", inline=False)
    # embed.add_field(name="We offer several fantastic opportunities for experienced and new Discord users to share ideas, exchange advice, listen to informative stage events, receive feedback, collaborate, and create impactful communities.🌿", value="\u200B", inline=False)

    return embed


# Profile Embed
def profile_embed(user_id):

    # query database
    session = get_session()
    profile = session.query(Profile).filter(
        Profile.user_id == str(user_id)).first()

    user = profile.user
    user_id = profile.user_id
    department = profile.department
    title = profile.title

    embed = discord.Embed(
        title="Discord bot Personal Profile",
        color=0xe6e6e6
    )

    embed.set_thumbnail(
        url="https://upload.wikimedia.org/wikipedia/en/thumb/6/63/Tsmc.svg/640px-Tsmc.svg.png")

    embed.add_field(name="User", value=user, inline=True)
    embed.add_field(name="Title", value=title, inline=True)
    embed.add_field(name="ID", value=user_id, inline=True)
    embed.add_field(name="Department", value=department, inline=True)

    return embed

# list leave time embed
def leave_embed(user_id, leave_date):

    # query database...
    session = get_session()

    time_sheet_list = session.query(Leave_Sheet).filter(Leave_Sheet.user_id.ilike(
        f"%{user_id}%"), Leave_Sheet.leave_date.ilike(f"%{str(leave_date)}%")).all()

    try:
        user = str(time_sheet_list[0].user)
        department = time_sheet_list[0].department
        query_project_list = []

        for item in time_sheet_list:
            query_project_dict = {}
            query_project_dict['LeaveDate'] = item.leave_date
            query_project_dict['reason'] = item.reason
            query_project_dict['hours'] = item.hours
            if item.status == False:
                query_project_dict['status'] = "Unapproved 😞"
            else:
                query_project_dict['status'] = "Approved 😀"

            query_project_list.append(query_project_dict)

        query_project = [
            f"🕐 {item['LeaveDate']} ➤ 🎫 {item['reason']} ➤ {item['hours']} ➤ {item['status']}" for item in query_project_list]

        project_list = ""
        sum_hours = 0

        for item in query_project_list:
            sum_hours += int(item['hours'])

        for element in query_project:
            project_list += (element + "\n")

        embed = discord.Embed(
            title="🌳 Leave Sheet",
            color=0xe6e6e6,
        )

        embed.set_thumbnail(
            url="https://upload.wikimedia.org/wikipedia/en/thumb/6/63/Tsmc.svg/640px-Tsmc.svg.png")
        embed.add_field(name="***Name***", value=f"> {user}", inline=True)
        embed.add_field(name="***department***",
                        value=f"> {department}", inline=True)
        embed.add_field(name="***sum(hrs)***",
                        value=f"> {sum_hours}", inline=True)
        embed.add_field(name="***Discription***",
                        value=f"```{project_list}```", inline=False)

        return embed

    except Exception as e:
        print(e)

# 指令表單


def help_embed():

    embed = discord.Embed(
        title="Bot Commands",
        description="All bot commands listed below",
        color=0xa51212
    )

    embed.set_thumbnail(
        url="https://upload.wikimedia.org/wikipedia/en/thumb/6/63/Tsmc.svg/640px-Tsmc.svg.png")

    embed.add_field(name="/help", value="List all bot commands", inline=False)
    embed.add_field(name="/duty", value="fill the duty form", inline=False)
    embed.add_field(name="/application",
                    value="fill the application form", inline=False)

    return embed

# 工時列表
def timesheet_embed(user_id, date):

    # query database...
    session = get_session()

    time_sheet_list = session.query(Time_Sheet).filter(Time_Sheet.user_id.ilike(
        f"%{user_id}%"), Time_Sheet.datetime == str(date)).all()

    user = str(time_sheet_list[0].user)  # name
    datetime = str(date)
    department = time_sheet_list[0].department
    query_project_list = []

    try:
        for item in time_sheet_list:
            query_project_dict = {}
            query_project_dict['project'] = item.project
            query_project_dict['hours'] = item.hours
            query_project_list.append(query_project_dict)

        query_project = [
            f"🔖 {item['project']}  ➤  ⏱ {item['hours']} " for item in query_project_list]

        project_list = ""
        sum_hours = 0

        for item in query_project_list:
            sum_hours += int(item['hours'])

        for element in query_project:
            project_list += (element + "\n")

        embed = discord.Embed(
            title="🌵 TimeSheet",
            color=0xe6e6e6,
        )

        embed.set_thumbnail(
            url="https://upload.wikimedia.org/wikipedia/en/thumb/6/63/Tsmc.svg/640px-Tsmc.svg.png")
        embed.add_field(name="***Name***", value=f"> {user}", inline=True)
        embed.add_field(name="***department***",
                        value=f"> {department}", inline=True)
        embed.add_field(name="***datetime***", value=f"> {datetime}", inline=True)
        embed.add_field(name="***sum(hrs)***",
                        value=f"> {sum_hours}", inline=True)
        embed.add_field(name="***projects***",
                        value=f"```{project_list}```", inline=False)

        return embed
    except Exception as e:
        print(e)


# 加班列表
def overtime_embed(user_id, date):

    # query database...
    session = get_session()

    time_sheet_list = session.query(Overtime_Sheet).filter(Overtime_Sheet.user_id.ilike(
        f"%{user_id}%"), Overtime_Sheet.date.ilike(f"%{str(date)}%")).all()

    user = str(time_sheet_list[0].user)

    department = time_sheet_list[0].department
    query_project_list = []
    try:
        for item in time_sheet_list:
            query_project_dict = {}
            query_project_dict['project'] = item.project
            query_project_dict['hours'] = item.hours
            query_project_dict['date'] = item.date
            if item.status == False:
                query_project_dict['status'] = "Unapproved 😞"
            else:
                query_project_dict['status'] = "Approved 😀"

            query_project_list.append(query_project_dict)

        query_project = [
            f"🕖 {item['date']} ➤ 📝 {item['project']} ➤ 💥 {item['hours']} ➤ {item['status']} " for item in query_project_list]

        project_list = ""
        sum_hours = 0

        for item in query_project_list:
            sum_hours += int(item['hours'])

        for element in query_project:
            project_list += (element + "\n")

        embed = discord.Embed(
            title="🔥 Overtime",
            color=0xe6e6e6,
        )

        embed.set_thumbnail(
            url="https://upload.wikimedia.org/wikipedia/en/thumb/6/63/Tsmc.svg/640px-Tsmc.svg.png")
        embed.add_field(name="***Name***", value=f"> {user}", inline=True)
        embed.add_field(name="***department***",
                        value=f"> {department}", inline=True)
        embed.add_field(name="***sum(hrs)***",
                        value=f"> {sum_hours}", inline=True)
        embed.add_field(name="***overtime***",
                        value=f"```{project_list}```", inline=False)

        return embed
    except Exception as e:
        print(e)


# 刪除加班
def delete_overtime_embed(user_id, date, project):

    # query database...
    try:
        session = get_session()

        time_sheet_list = session.query(Overtime_Sheet).filter(Overtime_Sheet.user_id.ilike(
            f"%{user_id}%"), Overtime_Sheet.date.ilike(f"%{str(date)}%"), Overtime_Sheet.project.ilike(f"%{str(project)}%")).first()

        session.delete(time_sheet_list)
        session.commit()

        embed = overtime_embed(user_id, date)

        return embed

    except Exception as e:
        print(e)


# 刪除請假表單 待修改
def delete_leave_embed(user_id, leave_date, reason):

    # query database...
    try:
        session = get_session()

        time_sheet_list = session.query(Leave_Sheet).filter(Leave_Sheet.user_id.ilike(
            f"%{user_id}%"), Leave_Sheet.leave_date.ilike(f"%{str(leave_date)}%"), Leave_Sheet.reason.ilike(f"%{str(reason)}%")).first()

        print(time_sheet_list)
        session.delete(time_sheet_list)
        session.commit()

        embed = welcome_leave_embed(user_id, leave_date)

        return embed

    except Exception as e:
        print(e)


# 刪除工時表單
def delete_timesheet_embed(user_id, date, project):

    # query database...
    try:
        session = get_session()

        time_sheet_list = session.query(Time_Sheet).filter(Time_Sheet.user_id.ilike(
            f"%{user_id}%"), Time_Sheet.datetime.ilike(f"%{str(date)}%"), Time_Sheet.project.ilike(f"%{str(project)}%")).first()

        session.delete(time_sheet_list)
        session.commit()

        embed = timesheet_embed(user_id, date)

        return embed

    except Exception as e:
        print(e)

# ----------------------------------------------------------------------------------------

# 插入工時


async def insert_timesheet(user, user_id, datetime, project, hours, department):

    session = get_session()
    TIMESHEET_DATA = []

    TIMESHEET_DATA = Time_Sheet(
        user=str(user),
        user_id=str(user_id),
        department=str(department),
        datetime=str(datetime),
        project=str(project),
        hours=str(hours)
    )

    session.merge(TIMESHEET_DATA)
    session.commit()

# 插入請假
async def insert_leavetime(user, user_id, apply_date, leave_date, reason, hours, department):

    session = get_session()

    LEAVETIME_DATA = []

    LEAVETIME_DATA = Leave_Sheet(
        user=str(user),
        user_id=str(user_id),
        reason=str(reason),
        department=str(department),
        apply_date=str(apply_date),
        leave_date=str(leave_date),
        hours=str(hours),
        status=False
    )

    session.merge(LEAVETIME_DATA)
    session.commit()

# 插入加班
async def insert_overtime(user, user_id, date, project, hours, department):

    session = get_session()

    OVERTIME_DATA = []

    OVERTIME_DATA = Overtime_Sheet(
        user=str(user),
        user_id=str(user_id),
        department=str(department),
        date=str(date),
        project=str(project),
        hours=str(hours),
        status=False
    )

    session.merge(OVERTIME_DATA)
    session.commit()