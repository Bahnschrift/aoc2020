open System
open System.IO
open Microsoft.FSharp.Core.Operators.Checked

[<EntryPoint>]
let main argv =
    let timer = Diagnostics.Stopwatch.StartNew()
    let data = File.ReadAllLines(Path.Combine(Directory.GetParent(Directory.GetParent(__SOURCE_DIRECTORY__).FullName).FullName, "inputs/03.txt"))
    let mutable part1 = int64 0
    let mutable part2 = int64 0
    
    let toboggan right down = 
        let mutable c = 0
        let mutable x = 0
        let mutable y = 0
        while y < data.Length do
            if data.[y].[x] = '#' then
                c <- c + 1
            x <- (x + right) % String.length data.[0]
            y <- y + down

        int64 c
    
    part1 <- toboggan 3 1
    part2 <- toboggan 1 1 * part1 * toboggan 5 1 * toboggan 7 1 * toboggan 1 2

    timer.Stop()
    printfn "Part 1: %i" part1
    printfn "Part 2: %i" part2
    printfn "Time: %fs" timer.Elapsed.TotalSeconds

    0