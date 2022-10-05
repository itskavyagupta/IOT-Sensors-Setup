import csv

class System:
    def __init__(self):
        self.sensors_list = list()
        self.sensor_mapping_list = list()
        self.master_node_list = list()
        self.freq = []
        self.size = int
        
    def config_system(self, file):
        data_file = open(file, 'r')
        reader = csv.DictReader(data_file)
        for row in reader:
            node_id = row['Node ID']
            type = row['Type']
            master_node_id = row['Master Node ID']
            
            if type == 'Master':
                self.master_node_list.append(int(master_node_id))
            elif type == "Sensor":
                self.sensors_list.append(int(node_id))
                self.sensor_mapping_list.append(int(master_node_id))
                
        
    def SensorAssignedCount(self, mapping_list, l, r, OverloadSensor):
        count = 0
        for i in range(l, r+1):
            if (mapping_list[i] == OverloadSensor): 
                count +=  1
        return count
    
    def OverloadNodeHelper(self,l, r):
        #creating a function to perform merge sort on sensor_mapping_list
        def mergeSort(mapping_list):
            
            if len(mapping_list) > 1:
                #finding the middle of the list
                mid = len(mapping_list) // 2
                #dividing the list into two halves
                left = mapping_list[:mid]
                right = mapping_list[mid:]
        
                #sorting the first half
                mergeSort(left)
                #sorting the second half
                mergeSort(right)
                
                #initialising iterators
                i = 0   #for first half
                j = 0   #for second half
                k = 0   #for the main list
        
                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        mapping_list[k] = left[i]
                        i += 1
                    else:
                        mapping_list[k] = right[j]
                        j += 1
                    k += 1
            
                while i < len(left):
                    mapping_list[k] = left[i]
                    i += 1
                    k += 1
                while j < len(right):
                    mapping_list[k]=right[j]
                    j += 1
                    k += 1
        
        #calling the mergesort function to sort the self.sensor_mapping_list
        mergeSort(self.sensor_mapping_list)
        
        #Using Binary Search to find the first occurrence of a given sensor in a sorted sensor_mapping_list
        def findFirstOccurrence(nums, left, right, TargetSensor):
            #initialize the result by -1
            result = -1
            
            while left <= right:
                #find the mid-value in the search space and compare it with the TargetSensor
                mid = (left + right) // 2
 
                #if the TargetSensor is located, update the result and search towards the left (lower indices)
                if TargetSensor == nums[mid]:
                    result = mid
                    right = mid - 1
 
                #if the TargetSensor is less than the middle element, discard the right half
                elif TargetSensor < nums[mid]:
                    right = mid - 1
 
                #if the TargetSensor is more than the middle element, discard the left half
                else:
                    left = mid + 1
 
            #return the leftmost index, or -1 if the TargetSensor is not found
            return result

        #Using Binary Search to find the last occurrence of a given sensor in a sorted sensor_mapping_list
        def findLastOccurrence(nums, left, right, TargetSensor):
            #initialize the result by -1
            result = -1
 
            while left <= right:
 
                #find the mid-value in the search space and compares it with the TargetSensor
                mid = (left + right) // 2
 
                #if the TargetSensor is located, update the result and search towards the right (higher indices)
                if TargetSensor == nums[mid]:
                    result = mid
                    left = mid + 1
 
                #if the TargetSensor is less than the middle element, discard the right half
                elif TargetSensor < nums[mid]:
                    right = mid - 1
 
                #if the TargetSensor is more than the middle element, discard the left half
                else:
                    left = mid + 1
 
            #return the leftmost index, or -1 if the TargetSensor is not found
            return result

        #calculating the number of device each master node serves
        for item in self.master_node_list:
            #finding first and last occurences of a particular sensor
            left = findFirstOccurrence(self.sensor_mapping_list, l, r, item)
            right = findLastOccurrence(self.sensor_mapping_list, l, r, item)
            #finding the total count of the given device by calling the SensorAssignedCount function
            self.freq.append(self.SensorAssignedCount(self.sensor_mapping_list, left, right, item))
        
        self.size=len(self.sensor_mapping_list)
        
        #initialising a list to store all the master nodes that might be overloaded
        k=list()
        #identifying the master node(s) that are overloaded
        for i in range(len(self.master_node_list)):
            if self.freq[i] >= self.size/2:
                k.append(self.master_node_list[i])
            else:
                pass
        if not k:
            return -1
        else:
            #returning the list without brackets to match the given sample output
            k = str(k)[1:-1]
            return (k)
        #pass
        
    def getOverloadedNode(self):
        return self.OverloadNodeHelper(0, len(self.sensor_mapping_list)-1)
    
    def getPotentialOverloadNode(self):
        #initialising a list to store all the master nodes that might be partially overloaded
        k=list()
        #identifying the master node(s) that are partially overloaded
        for i in range(len(self.freq)):
            if (self.freq[i] < self.size/2) and (self.freq[i] >= self.size/3):
                k.append(self.master_node_list[i])
            else:
                pass
        if not k:
            return -1
        else:
            #returning the list without brackets to match the given sample output
            k = str(k)[1:-1]
            return (k)
        #pass
    
if __name__ == "__main__":
    test_system1 = System()
    
    test_system1.config_system('app_data1.csv')
    
    print("Overloded Master Node : ", test_system1.getOverloadedNode())
    
    print("Partially Overloaded Master Node : ", test_system1.getPotentialOverloadNode())

    test_system2 = System()
    
    test_system2.config_system('app_data2.csv')
    
    print("Overloded Master Node : ", test_system2.getOverloadedNode())
    
    print("Partially Overloaded Master Node : ", test_system2.getPotentialOverloadNode())

    test_system3 = System()

    test_system3.config_system('app_data3.csv')
    
    print("Overloded Master Node : ", test_system3.getOverloadedNode())
    
    print("Partially Overloaded Master Node : ", test_system3.getPotentialOverloadNode())

    test_system4 = System()

    test_system4.config_system('app_data4.csv')
    
    print("Overloded Master Node : ", test_system4.getOverloadedNode())
    
    print("Partially Overloaded Master Node : ", test_system4.getPotentialOverloadNode())
