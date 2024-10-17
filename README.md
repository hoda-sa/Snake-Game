# Snake Game

This is a classic Snake game implementation using Python's Turtle graphics library. The game features a snake that grows longer as it eats food, with the goal of achieving the highest score possible without colliding with the walls or its own tail.

## Features

- Snake movement controlled by arrow keys
- Randomly spawning food
- Score tracking
- High score persistence between game sessions
- Game over on wall or tail collision
- Snake growth upon eating food

## Files

- `main.py`: The main game loop and setup
- `snake.py`: Contains the Snake class, managing snake behavior
- `food.py`: Manages the food object in the game
- `scoreboard.py`: Handles score display and tracking
- `data.txt`: Stores the high score

## How to Run

1. Ensure you have Python installed on your system.
2. Install the required libraries (only built-in libraries are used, so no additional installation should be necessary).
3. Run the game by executing the `main.py` file:

   ```
   python main.py
   ```

4. Use the arrow keys to control the snake:
   - Up Arrow: Move Up
   - Down Arrow: Move Down
   - Left Arrow: Move Left
   - Right Arrow: Move Right

5. Try to eat as much food as possible without colliding with the walls or the snake's own tail.
6. The game will automatically reset when you collide, and your high score will be saved.

## Game Controls

- **Up Arrow**: Move the snake upwards
- **Down Arrow**: Move the snake downwards
- **Left Arrow**: Move the snake to the left
- **Right Arrow**: Move the snake to the right

## Customization

You can customize various aspects of the game by modifying the constants in the respective files:

- Change colors, shapes, or sizes in `food.py` and `snake.py`
- Adjust game speed by modifying the `time.sleep()` value in `main.py`
- Change the screen size or game boundary in `main.py`

## Contributing

Feel free to fork this project and make your own modifications. Some ideas for enhancements:
- Add obstacles
- Implement different levels of difficulty
- Create a start menu
- Add sound effects

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
