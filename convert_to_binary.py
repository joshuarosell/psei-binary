import pandas as pd

# Read the data
df = pd.read_csv('data.csv')

# Print original distribution
print(f'Original distribution:')
print(f'  DOWN: {(df["target"] == "DOWN").sum()}')
print(f'  FLAT: {(df["target"] == "FLAT").sum()}')
print(f'  UP: {(df["target"] == "UP").sum()}')
print()

# Remap FLAT entries based on price_change_pct
# FLAT with price_change_pct < 0 → Down
df.loc[(df['target'] == 'FLAT') & (df['price_change_pct'] < 0), 'target'] = 'Down'
# FLAT with price_change_pct >= 0 → Up
df.loc[(df['target'] == 'FLAT') & (df['price_change_pct'] >= 0), 'target'] = 'Up'

# Convert DOWN → Down and UP → Up for consistency
df.loc[df['target'] == 'DOWN', 'target'] = 'Down'
df.loc[df['target'] == 'UP', 'target'] = 'Up'

# Update encoding: Down = 0.0, Up = 1.0
df.loc[df['target'] == 'Down', 'target_encoded'] = 0.0
df.loc[df['target'] == 'Up', 'target_encoded'] = 1.0

# Print updated distribution
print(f'Updated distribution:')
print(f'  Down: {(df["target"] == "Down").sum()}')
print(f'  Up: {(df["target"] == "Up").sum()}')
print()

# Save the updated data
df.to_csv('data.csv', index=False)
print('✓ data.csv updated successfully')
print(f'✓ Binary encoding: Down=0.0, Up=1.0')
