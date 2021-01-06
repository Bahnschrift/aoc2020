open System
open System.IO

[<EntryPoint>]
let main argv =
    let timer = Diagnostics.Stopwatch.StartNew()
    // Surely there's a better way to do this
    let data = Array.map int (File.ReadAllLines(Path.Combine(Directory.GetParent(Directory.GetParent(__SOURCE_DIRECTORY__).FullName).FullName, "inputs/01.txt")))
    let mutable part1 = 0
    let mutable part2 = 0

    for x in data do
        for y in data do
            if x + y = 2020 then
                part1 <- x * y
            for z in data do
                if x + y + z = 2020 then
                    part2 <- x * y * z

    timer.Stop()
    printfn "Part 1: %i" part1
    printfn "Part 2: %i" part2
    printfn "Time: %fs" timer.Elapsed.TotalSeconds
    
    0