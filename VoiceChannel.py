import discord

async def Voice(member, before, after):
    global role
    if member.nick == None:
        channel = await after.channel.clone(name=f"{member.name}'s channel")
    else:
        channel = await after.channel.clone(name=f"{member.nick}'s channel")

    await member.move_to(channel)
    if len(after.channel.members) == 1:
        role = await after.channel.guild.create_role(name=f'{after.channel.name} owner', color=discord.Color(633573),
                                                    reason='Channel owner')
        await after.channel.set_permissions(role, overwrite=discord.PermissionOverwrite(manage_channels=True, connect=True,
                                                                                        speak=True, stream=True,
                                                                                        view_channel=True))
        await member.add_roles(role)

    if str(before.channel) != '➕ Erstelle Channel' and str(before.channel) != 'None' and str(before.channel) != '🎵 Musik':
        if before.channel.category.name == '⋙ 🎤 Voice Channels ⋘' or '🎤 Voice Channels':
            if len(before.channel.members) == 0:
                await member.remove_roles(role)
                await before.channel.delete()
                await role.delete()