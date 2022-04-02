const NAMES = [
    'white',
    'lightgray',
    'darkgray',
    'black',
    'lightpink',
    'red',
    'orange',
    'brown',
    'yellow',
    'lightgreen',
    'green',
    'cyan',
    'grayblue',
    'blue',
    'pink',
    'purple'
  ]

  const COLORS = [
    [255, 255, 255],
    [228, 228, 228],
    [136, 136, 136],
    [34, 34, 34],
    [255, 167, 209],
    [229, 0, 0],
    [229, 149, 0],
    [160, 106, 66],
    [229, 217, 0],
    [148, 224, 68],
    [2, 190, 1],
    [0, 211, 221],
    [0, 131, 199],
    [0, 0, 234],
    [207, 110, 228],
    [130, 0, 128]
  ]

for (let i = 0; i < NAMES.length; i++) {
    let name = NAMES[i]
    let color = COLORS[i]
    let rgb = `(${color[0]}, ${color[1]}, ${color[2]}, 255)`
    console.log(`${rgb}: '${name}',`)
}

for (let i = 0; i < NAMES.length; i++) {
    let name = NAMES[i]
    let color = COLORS[i]
    let rgb = `(${color[0]}, ${color[1]}, ${color[2]}, 255)`
    console.log(`'${name}': ${rgb},`)
}