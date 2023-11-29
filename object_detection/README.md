# Object Detection

- Template Matching
  - Simply looking for an exact copy of an image in another image.

- Corner Detection 
  - Looking for corners in images.

- Edge Detection
  - Expanding to find general edges of objects.

- Grid Detection
  - Combining both concepts to find grids in images.

- Contour Detection
  - Allows us to detect foreground vs background images.
  - Also allows for detection of external vs internal contours (e.g. grabbing the eyes and smile from a cartoon smile face).

## Feature Matching
Advanced methods of detecting matching objects in another image, evenn if the target image is not shown exactly the same in the image we are searching

## Watershed Algorithm
Advanced algorithm that allows us to segment images into foreground and background, also allows us to manually set seeds to choose segments of an image.

## Facial and Eye Detection
We'll use Haar Cascades to detect faces in images, this isn't yet facial recognition, that requires deep learning which will be present in future section.


