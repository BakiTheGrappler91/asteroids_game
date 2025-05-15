## 🪐 Asteroids Game (Python + Pygame)
A classic-style Asteroids arcade game built using Python and Pygame! Pilot your ship through space, dodge asteroids, and blast them into smaller fragments to increase your score. This project showcases foundational 2D game development concepts including physics, collisions, and screen wrap-around.
<br/><br/>

### 🎮 Features
🚀 Player-controlled spaceship with rotation, thrust, and drag

💥 Asteroids split on impact into smaller fragments

🎯 Projectile firing system with cooldown

🔁 Screen edge wrap-around for both the ship and projectiles

🧠 Collision detection using pixel-perfect masking

🧮 Scoring system and life counter

📋 Main menu system (Play screen)
<br/><br/>

### 🕹️ Controls
| Action |	Key |
| ------- | ------- |
| Rotate Left |	← Arrow |
| Rotate Right |	→ Arrow |
| Thrust |	↑ Arrow |
| Shoot |	Spacebar |
| Quit |	Close window |

<br/><br/>

### 📸 Gameplay
![](https://github.com/BakiTheGrappler91/asteroids_game/blob/main/asteroids_gif.gif)
<br/><br/>

### 📁 Project Structure
asteroid_game/
<br/>
├── game.py                    # Main game loop and menu
<br/>
├── scripts/
<br/>
│   ├── entities.py            # Ship, Asteroid, and PhysicsEntity classes
<br/>
│   └── projectiles.py         # Bullet (Projectile) class
<br/><br/>

### 🧠 How It Works
- Ship physics include drag, acceleration, and rotation.

- Asteroids move randomly and split in half when shot (if large enough).

- Collision detection is done via pixel-level masks (pygame.mask).

- Bullets expire after a short lifespan and wrap around the screen.

- Score increments with each asteroid destroyed.

- Lives decrease upon collision with an asteroid; game restarts from menu on death.
<br/><br/>

### 🛠️ Getting Started
1. Clone the Repository<br/>
git clone https://github.com/BakiTheGrappler91/asteroids_game<br/>
cd asteroids_game

2. Install Requirements<br/>
pip install pygame

3. Run the Game<br/>
python game.py
<br/><br/>

### 🧪 Built With
Python 3

Pygame — for graphics, input, and sound
<br/><br/>

### 📝 Acknowledgments
This project is inspired by classic Asteroids arcade games and implemented using custom-built physics and collision systems.
