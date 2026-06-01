import asyncio
import time
points = 0
point_gain = 10
async def tick():
    global points, point_gain
    points += point_gain
    print(f'gained {point_gain} points.')
    time.sleep(1)
async def yell():
    global points, point_gain
    print(f"You are on {points} points.")
    time.sleep(2)
async def main():
    await asyncio.gather(tick(), yell())
while True:
    asyncio.run(tick())
    asyncio.run(yell())