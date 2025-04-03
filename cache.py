
def offset(ADDR, x):
  return ADDR % x

def index(ADDR, x, y):
  return (ADDR // x) % y

def tag(ADDR, x, y):
  return (ADDR // x) // y

# Get user input
hex_address = input("Enter a hex address (e.g., 0x3F4): ")
bytes_per_block = int(input("Enter bytes per block (x): "))
num_sets = int(input("Enter number of sets (y): "))

# Convert hex to int
ADDR = int(hex_address, 16)

# Compute values
off = offset(ADDR, bytes_per_block)
idx = index(ADDR, bytes_per_block, num_sets)
tg = tag(ADDR, bytes_per_block, num_sets)

# Output result
# Output result
print(f"\nAddress breakdown:")
print(f"Tag   : {hex(tg)}")
print(f"Index : {hex(idx)}")
print(f"Offset: {hex(off)}")

