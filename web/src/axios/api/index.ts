import hyRequest from '../index'
import { IDataType } from './types'
enum screenApi {
    WordCloud = 'wordcloud',
    carbon = 'china_carbon',
    World = 'global_top'
}
export function GetListTestRequest() {
    return hyRequest.get<IDataType<any>>({
        url: screenApi.WordCloud
    })
}
export function getCarbonReqeust(){
    return hyRequest.get<IDataType<any>>({
        url: screenApi.carbon, 	//need to add slash at the end of the u
    })
}
export function getWorldReqeust(){
    return hyRequest.get<IDataType<any>>({ 
        url:screenApi.World, 	
    })
}