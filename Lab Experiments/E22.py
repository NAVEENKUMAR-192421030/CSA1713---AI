planets = {
    "Mercury": "Smallest Planet",
    "Venus": "Hottest Planet",
    "Earth": "Planet with Life",
    "Mars": "Red Planet",
    "Jupiter": "Largest Planet",
    "Saturn": "Planet with Rings",
    "Uranus": "Ice Giant",
    "Neptune": "Farthest Planet"
}

print("Planets Database")

for planet, description in planets.items():
    print(planet, ":", description)
