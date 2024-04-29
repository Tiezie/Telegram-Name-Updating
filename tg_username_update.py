async def change_name_auto():
    print('Will change name')

    while True:
        try:
            time_cur = strftime("%H:%M:%S:%p:%a", time.localtime())
            hour, minu, seco, p, abbwn = time_cur.split(':')
            
            if seco == '00' or seco == '30':
                shift = 0
                mult = 1
                if int(minu) > 30:
                    shift = 1

                # Determine the appropriate clock emoji based on the current hour
                hsym = time_emoji_symb[(int(hour) % 12) * 2 + shift]

                # Update last name with the chosen clock emoji
                last_name = '%s时%s分 %s' % (hour, minu, hsym)
                await client1(UpdateProfileRequest(last_name=last_name))
                logger.info('Updated -> %s' % last_name)

        except KeyboardInterrupt:
            print('\nWill reset last name\n')
            await client1(UpdateProfileRequest(last_name=''))
            sys.exit()

        except Exception as e:
            print('%s: %s' % (type(e), e))

        await asyncio.sleep(1)
