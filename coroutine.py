import asyncio


# Define a coroutine that simulates
# a time-consuming task
async def fetch_data(delay):
    print("Fetching data...")
    await asyncio.sleep(delay) # Simulate an I/O operation with a sleep
    print("Data fetched")
    return {"data": "some data"}

# Define another coroutine that calls the first coroutine
async def main():
    print("Start of main coroutine")
    task = fetch_data(2)  # Create coroutene fetch_data, HERE this coroutine doesn't start yes!!!!
    print("Coroutine fetch_data've been created!")
    # Await fetch_data coroutine, pausing execution of main untill
    # fetch_data completes
    result = await task  # Start execution coroutine fetch_data 
    print(f"Received result: {result}")
    print("End of main coroutines")

# Run the main coroutine
asyncio.run(main())




