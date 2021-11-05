 if SNAKE_POS[0] == -10:
        time_snake_postition = SNAKE_POS[0]   #тимчасова поз змії
        SNAKE_POS.insert(0, 710)
        SNAKE_POS.remove(SNAKE_POS[1])
        my_socket.send(pickle.dumps(SNAKE_POS))
        time.sleep(0.5)
        my_socket.send(pickle.dumps(SNAKE_BODY))
        SNAKE_POS.insert(0, time_snake_postition)
        SNAKE_POS.remove(SNAKE_POS[1])
