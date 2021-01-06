open System
open System.IO
open Microsoft.FSharp.Core.Operators.Checked

[<EntryPoint>]
let main argv =
    let timer = Diagnostics.Stopwatch.StartNew()
    let data = File.ReadAllText(Path.Combine(Directory.GetParent(Directory.GetParent(__SOURCE_DIRECTORY__).FullName).FullName, "inputs/06.txt")).Split("\r\n\r\n")
    let mutable part1 = 0
    let mutable part2 = 0

    for group in data do
        let group = group.Split("\r\n")
        let mutable union = Set group.[0]
        let mutable intersection = Set group.[0]
        for person in group.[1 .. ] do
            union <- Set.union union (Set person)
            intersection <- Set.intersect intersection (Set person)
        part1 <- part1 + union.Count
        part2 <- part2 + intersection.Count
    
    timer.Stop()
    printfn "Part 1: %i" part1
    printfn "Part 2: %i" part2
    printfn "Time: %fs" timer.Elapsed.TotalSeconds

    0