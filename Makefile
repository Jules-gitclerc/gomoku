all:
	cp pbrain-gomoku-ai.py pbrain-gomoku-ai
	chmod +x pbrain-gomoku-ai

clean:

fclean: clean
	rm -f pbrain-gomoku-ai

re: fclean all