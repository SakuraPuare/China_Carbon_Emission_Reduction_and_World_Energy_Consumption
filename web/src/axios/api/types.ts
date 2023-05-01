export interface IWordCloud {
    value: number,
    name: string,
    length: number,
}
export interface IChina {
    china: any[]
}
export interface IAnnualUse {
    annualUse: any[]
}
export interface test {
    list: any[]
}
export interface IWorldList {
    WorldList: any[],
    length: number,
}
export interface IDataType<T = any> {
    code: number
    error: string
    success: string
    error_message: string
    data: T
}