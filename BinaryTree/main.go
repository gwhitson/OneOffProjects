package main

import (
    "fmt"
)

type TreeNode struct {
    val     int
    left    *TreeNode
    right   *TreeNode
}

type BinaryTree struct {
    nodes   []TreeNode
    len     int
    root    *TreeNode
}

func CreateTree(nums []int) BinaryTree {

    tree := BinaryTree{
        []TreeNode{},
        0,
        nil,
    }

    for _, num := range nums {
        // create a node struct
        node := TreeNode{
            num,
            nil,
            nil,
        }
        // empty tree, assign element found as root
        if tree.root == nil {
            tree.root = &node
        } else {
            // declare a slice to use like a queue
            queue := []*TreeNode{tree.root}

            // while queue is not empty
            for len(queue) != 0 {
                top := queue[0]
                // if the new nodes value is less than the current one being
                // compared, either set it as the left child if none exists
                // or add the left child to the queue
                if node.val < top.val {
                    if top.left != nil {
                        top.left = &node
                    } else {
                        queue = append(queue, top.left)
                    }
                } else if node.val > top.val {
                    if top.right != nil {
                        top.right = &node
                    } else {
                        queue = append(queue, top.right)
                    }
                } else {
                    fmt.Printf("%v\n", tree.nodes)
                }

                // pop queue
                queue = queue[1:]
            }

        }
        tree.nodes = append(tree.nodes, node)
        tree.len++
    }
    return tree
}

func main () {
    nums := []int{2,5,7,8,9,11,15,16,92}
    out := CreateTree(nums)
    fmt.Printf("%v\n", out)
}
