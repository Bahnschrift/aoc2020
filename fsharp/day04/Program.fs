open System
open System.IO
open System.Collections.Generic
open Microsoft.FSharp.Core.Operators.Checked

[<EntryPoint>]
let main argv =
    let timer = Diagnostics.Stopwatch.StartNew()
    let data = File.ReadAllText(Path.Combine(Directory.GetParent(Directory.GetParent(__SOURCE_DIRECTORY__).FullName).FullName, "inputs/04.txt")).Split("\r\n\r\n")
    let mutable part1 = 0
    let mutable part2 = 0
    
    for passport in data do
        let profile = new Dictionary<string, string>()
        let fields = (passport.Split "\r\n" |> String.concat " ").Split " "
        let mutable cid = false
        for field in fields do
            let fieldValPair = field.Split ':'
            profile.Add(fieldValPair.[0], fieldValPair.[1])
            if fieldValPair.[0] = "cid" then
                cid <- true
        let part1Valid = (fields.Length = 8) || (fields.Length = 7 && not cid)
        if part1Valid then
            part1 <- part1 + 1

            let mutable part2Valid = true
            if 1920 > int profile.["byr"] || int profile.["byr"] > 2002 then part2Valid <- false
            else if 2010 > int profile.["iyr"] || int profile.["iyr"] > 2020 then part2Valid <- false
            else if 2020 > int profile.["eyr"] || int profile.["eyr"] > 2030 then part2Valid <- false
            else if not (List.contains (profile.["hgt"].[String.length profile.["hgt"] - 2 .. ]) ["in";"cm"])
                || ((profile.["hgt"].[String.length profile.["hgt"] - 2 .. ] = "cm") && int profile.["hgt"].[ .. String.length profile.["hgt"] - 3] |> fun x -> 150 > x || x > 193) 
                || ((profile.["hgt"].[String.length profile.["hgt"] - 2 .. ] = "in") && int profile.["hgt"].[ .. String.length profile.["hgt"] - 3] |> fun x -> 59 > x || x > 76)
            then part2Valid <- false    
            else if profile.["hcl"].[0] <> '#' || String.length profile.["hcl"] <> 7 || not (profile.["hcl"].[1 .. ] |> Seq.forall(fun x -> Char.IsDigit x || List.contains x ['a';'b';'c';'d';'e';'f'])) then part2Valid <- false
            else if not (Array.contains profile.["ecl"] ("amb blu brn gry grn hzl oth".Split(" "))) then part2Valid <- false
            else if String.length profile.["pid"] <> 9 || not (profile.["pid"] |> Seq.forall Char.IsDigit) then part2Valid <- false

            if part2Valid then part2 <- part2 + 1

    timer.Stop()
    printfn "Part 1: %i" part1
    printfn "Part 2: %i" part2
    printfn "Time: %fs" timer.Elapsed.TotalSeconds

    0